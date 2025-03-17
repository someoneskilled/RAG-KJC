# 🏫 KJC College Chatbot - RAG-Based System

This is a **RAG (Retrieval-Augmented Generation) based chatbot** for **Kristu Jayanti College** that can **answer queries** about events, programs, achievements, faculty, locations, amenities, and more.  

It uses **Llama 3 via Groq API** as the foundational model and retrieves relevant context from a **text file (TXT)** containing college-related information.

---

## 📌 Features
✅ **Text-Based Data Handling** – Uses a simple `TXT` file instead of a complex database.  
✅ **Chunking & Matching** – Splits data into smaller pieces and finds the most relevant chunk for a query.  
✅ **LLM-Powered Responses** – Uses `Llama 3 (via Groq)` to generate natural, context-aware answers.  
✅ **Lightweight & Easy to Maintain** – No vector DB, just a Python script and a TXT file.  

---

## 🔧 How It Works (Flow)
### **1️⃣ Data Preparation**
- The chatbot reads a **TXT file (`dirtydata.txt`)** containing all college-related information.
- The text is **split into chunks** of ~500 words for efficient retrieval.

### **2️⃣ Query Processing**
- When a user asks a question, the bot **compares it** with available text chunks.
- It finds the **most relevant chunk** using `difflib` (text similarity matching).

### **3️⃣ Response Generation**
- The retrieved chunk is sent to **Llama 3 (via Groq API)**.
- The model **processes the query with the context** and generates an accurate response.

### **4️⃣ User Interaction**
- The response is displayed, and the chatbot waits for the next query.
- The user can exit anytime by typing **"exit"** or **"quit"**.

---

