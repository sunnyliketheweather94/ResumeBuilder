# JobHunter 
This repository will store the code that allows the user to construct a resume and use ChatGPT to modify the resume. More specifically, you can add fields to the resume such as:
1. Relevant skills
2. Professional experiences 
3. Relevant projects (if any)
4. Education

Once you populate the resume, you can then use ChatGPT to modify the professional experiences' outcomes, as deemed necessary. In order to do this, it is assumed that you have a file called `.configs.ini` where the `organization` and `api_key` are stored; these will be necessary for the OpenAI API so that you can then call ChatGPT. We use the `gpt-3.5-turbo` model here. You can create this file by replacing the `ORGANIZATION` and `API_KEY` strings in [configs.py](./configs.py) for your convenience. 

In order to run this little app, you should create your virtual environment, install the dependencies inside of [requirements.txt](./requirements.txt) and then run `python job-hunter.py`. There are tests inside of the `main` function inside [`job-hunter.py`](./job_hunter.py) for you to modify and play around with.