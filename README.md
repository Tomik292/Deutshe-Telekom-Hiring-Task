# Assignment for applicants to the position Python Developer for LLM agent solutions

**Dear candidate**,

We hope you're doing( well! We are excited about your potential as a Senior Python Developer for LLM solutions on our team. Your skills and experience have truly impressed us.
As part of our evaluation process, we have a little challenge for you to master.

To successfully complete the hiring task, we kindly ask you to adhere to the following requirements:

- **Python**: Utilize Python programming language (eventually also Jupyter Notebooks) for creating the solution. Showcase your coding skills and proficiency in handling data and large language models via APIs (or locally).
- **Clear Workflow Explanation**: Provide a step-by-step explanation of your workflow and the techniques employed in building the classification model. This should be documented in either a Jupyter Notebook or an accompanying document.
- **Document follow-up ideas**: By far, noone will produce a perfect solution within these 5 days, but you will have a full backlog of ideas what to do in order to optimize and develop the solution further.
  Please document them all and give us some hints how you would implement the enhancements. Again, you can do this in a notebook or separate document.

## The Challenge

Build a small RAG (Retrieval-Augmented Generation) solution using Deutsche Telekom press releases.
Your final product should include:

- a data store (can be a document-based DB, SQL DB or Vector DB)
- a data ingestion / indexing service
- a retrieval service / component for finding matching documents
- a connection to any public LLM service, which it prompts for a good answer
- some interactive component that we can deploy on our systems and that we can ask questions about announcements and publications of Deutsche Telekom.
  The interactive part might be a simple notebook, a streamlit app or a full-fledged JS web application (based on any open source framework). Surprise us!
- not necessarily it has to be a chatbot, we will ask singular questions
- Non-Functional requirements:
  - The solution needs to be capable to handle several requests (5-10) in parallel and has to provide
    options for further scaling
  - The response time for a query / request needs to be below 5 seconds

## The Rules

- Use whatever open source framework is available for which the license allows commercial use (MIT / Apache 2.0 or similar). You must not use commercial products that require a license key nor open source frameworks that exclude commercial usage (CC BY-NC licenses).

- Use cloud services (such as Azure, GCP, AWS) if this is your personal account. If you are employed at a company using the hyperscaler services, please do not (mis)use their account for it.
  Beware that with using those services, you will have to reveal the related API Access Tokens.

- If you are using public services of OpenAI or if you use any model available on huggingface you do not need to reveal the access key. We will adapt it to use our access keys.

- Submit your results either in a GitHub repository or a zip file or any similar
  appropriate format. If you use a private repository (not to show anyone else what you are working on), please ask us for the username that should get access on it.

## The Data

- 250 press releases of Deutsche Telekom
- The data was scraped from our website and cleaned from any HTML/CSS/Script markup.
- The language of all texts is English.
- There is no formatting or structure as it is plain text (you don't need to care about parsing).

We're eagerly looking forward to seeing your brilliance in action!

If you have any questions or need any support while working on the task, don't hesitate to reach out to us at [j.kondek@telekom.com](j.kondek@telekom.com). We're here to assist you throughout the process.

Best regards,
<br>Jakub Kondek
<br>Senior Data Scientist
