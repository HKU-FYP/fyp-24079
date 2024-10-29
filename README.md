# Final Year Project: LLM-based Real-time Personalized Financial News Notification System

### Project Description 

In today’s fast-paced financial markets, which operates in real-time and is highly sensitive to news and sentiments, tracking news in real-time is crucial. Investor often find it challenging to determine the relevance of news to their own portfolios and to track such information efficiently, even in real-time.
To address this issue, we propose developing an LLM-based real-time personalized financial news alert application.

This application aims to offers a website which allows users to input their investment portfolio and receive real-time notifications about relevant news with a summary of the news and an impact to the user portfolio. This ensures that users receive only the most relevant updates, enabling them to focus on news that matters for their financial decisions. Also, the content summary will help users quickly grasp key insights and suggest them which articles worth reading in full. 

By providing timely and relevant updates, this project will help individual investors make informed and quick decisions, empowering them to stay ahead in the financial markets with ease.

### Project Objectives

The primary objective of this project is to develop a personalized real-time financial news notification application that leverages LLMs and Natural Language Processing (NLP) to deliver highly relevant and time-sensitive information to investors. This application aims to enable retail investors to make informed decisions quickly and effectively by delivering summarized news updates and insights. The breakdown of the main objective includes:

1. Delivery of personalized notifications <br />
One of the objectives is to provide investors with personalized notifications on financial news that directly affects their portfolio holdings. By leveraging LLMs and NLP, the system will filter and deliver news content tailored to their personalized preferences based on users' inputs regarding their portfolios. This ensures that users receive only the most relevant updates, enabling them to focus on news that matters for their financial decisions.


2. Summarization of key information <br />
The application aims to minimize the time retail investors spend reading and analyzing news articles by providing concise summaries. For each relevant article delivered through the notification, LLM-based content summarization will help users quickly grasp key insights and suggest them which articles are worth reading in full. This feature allows investors to make faster decisions without reviewing entire news.


3. Analysis of the news and prediction of stock price <br />
After identifying relevant news, LLMs will analyze the content of news articles to predict their potential impact on stock prices. This analysis will serve as a guide for retail investors in their decision-making. It will be conducted in real-time and delivered alongside each news notification, helping users make more informed investment decisions.

4. Interaction with LLM for further clarification <br />
To provide further analysis and insight on the selected news delivered to users, our system allows users to gain deeper insights by providing a chat function with LLM. This interactive feature aims to help users better understand the impact of news with more detailed information about certain news.

5. Real-time acquisition of data and delivery of notifications <br />
To ensure investors are updated immediately, the application aims to deliver real-time notifications using financial news APIs. The system is planned to poll relevant news sources continuously every few seconds. The combination of rapid news collection, LLM-based filtering, and instant notifications via email or social media messages ensures that stockholders receive timely updates, allowing them to act promptly on global market events.

### Proposed Project Architecture

![화면 캡처 2024-10-30 000034](https://github.com/user-attachments/assets/cf7a13d7-b12e-4443-b654-dff6c7336c0b)

The project is composed of a number of system components to deliver a personalized and real-time financial news notification system. Upon user registration, users can provide stock names or keywords to the system for personalized notification. If stock names are provided, the system queries more detailed stock information, such as stock industry and related keywords. Then, the fine-tuned large language model generates example keywords likely to impact the provided stock. For example, if a user enters ‘Coca Cola’, the generated example keywords may include ‘beverage industry trends’, ‘sugar tax impact’, or ‘global supply chain challenges’. These keywords are then converted into embeddings and stored in the Vector DB, which will be used for embedding search with the financial news article to extract only the relevant ones.
	
To ensure real-time delivery, a polling agent continuously polls the financial news website with a short interval (about 10 seconds). If there are any new articles, the agent will place them on the asynchronous message queue like RabbitMQ. Next, the Document Analyzer, continuously consuming the message queue, performs an embedding search between the article and each user’s stored keyword embeddings to calculate the relevance score.

If relevant, then the article is passed to the Stock Analyzer LLM which is fine-tuned to generate the news analysis including a brief summary and how the article might impact the user’s stock portfolio, which will be delivered to the user via email or SNS channels.

