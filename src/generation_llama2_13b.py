import boto3
import json
import re

# Integrating Foundation Models into Your Code with Amazon Bedrock

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2"
)

# prompt = description  # cannot contain /n
model_id = "meta.llama2-13b-chat-v1"
final_result = ""


def count_words(text):
    return len(re.findall(r'\b\w+\b', text))


def invoke_ai_model(user_prompt, model_id):

    prompt = f"""
        The following is weekly news:
        {user_prompt}
        Summarize the about news and key information in 100 words in complete sentences.
    """

    body = {
        "prompt": prompt,
        "max_gen_len": 100,
        # Higher temperature: more creative. Lower temperature: more deterministic responses
        "temperature": 0.7,
        # Below 1.0: consider only the most probable options and ignore less probable ones
        "top_p": 1
    }
    kwargs = {
        "modelId": model_id,
        "contentType": "application/json",
        "accept": "*/*",
        "body": json.dumps(body)
    }

    res = bedrock_runtime.invoke_model(**kwargs)
    res_body = json.loads(res.get("body").read())
    text_result = res_body.get("generation")

    return text_result

def caching_news_mechanism(raw_news):

    news_summary_list = [invoke_ai_model(each_news, model_id)
                         for each_news in raw_news]

    final_result = invoke_ai_model(
        "".join(news_summary_list).replace("\n", ""), model_id)

    print(final_result)

    return final_result
