## arXiv Assistant: A Research Paper Q&A Chatbot

This Streamlit application leverages the power of Langchain and large language models (LLMs) to answer your questions about research papers from arXiv.

**Features:**

- **arXiv Search:** Uses the `arxiv` tool from Langchain to search for relevant papers based on your queries.
- **Summarization:** Provides concise summaries of the retrieved papers.
- **Citations:** Includes citations for the papers used in generating the answer, ensuring credibility and transparency.
- **Choice of Provider:** Select between Google AI or OpenAI as your LLM provider.
- **Model Selection:** Choose from available models within your selected provider.

**Getting Started:**

1. **Installation:**

   ```bash
   pip install streamlit langchain langchain-google-genai openai pyperclip
   ```

2. **API Keys:**

   - Obtain API keys for either Google AI or OpenAI (or both) from their respective platforms.
   - Paste your API keys into the designated fields in the Streamlit sidebar.

3. **Run the Application:**

   ```bash
   streamlit run arXiv_agent.py
   ```

4. **Interact:**

   - Type your questions about arXiv papers in the text input box.
   - Click the "Ask" button.
   - The chatbot will provide a summarized answer with citations.

**Code Structure:**

- The code is organized into sections for API key management, model selection, tool loading, agent creation, and Streamlit interface setup.
- Comments explain the purpose of each section and key variables.

**Contributing:**

- Feel free to contribute by adding new features, improving the code, or fixing bugs.
- Submit pull requests with clear descriptions of your changes.

**License:**

This project is licensed under the GPL-3.0 license.

**Disclaimer:**

- The accuracy of the chatbot's responses depends on the quality of the data in arXiv and the capabilities of the chosen LLM.
- Always verify information from multiple sources.
