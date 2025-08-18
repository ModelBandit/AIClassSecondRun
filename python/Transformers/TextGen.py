from transformers import pipeline

text_generator = pipeline("text-generation", model="skt/kogpt2-base-v2")

prompt = "gpt2의 대답은 조현병에 걸린 환자와도 같았다."

result = text_generator(prompt, max_length=100, do_sample=True,
                        top_k=50,
                        top_p=0.95)
print(result[0]['generated_text'])
