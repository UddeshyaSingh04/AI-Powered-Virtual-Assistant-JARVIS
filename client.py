from openai import OpenAI

# client = openAI()
# pip install openai
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="s4k-proj-cFtIvUj3nd8sITcSCdUmZ3HrwiVSeYOWr1lbjZXXJE01AwBe4DMp2G-KVNWUobxAvpav0a5DK-T3BlbkFJtGrgQ8iM7Dgr6KDj8N01VRIyh8wxxcEfwUC-QVaMtnIGZkCMofs8cQaFwtZqqr34nzf7lkBloA",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Or any other model you want to use
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general task like Alexa and google cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

# Step 3: Print the reply
print(completion.choices[0].message.content)

# basically this program will not run because this OpenAI API is paid 

# so just we made a function and put in main program (check in main program)