
---

## **🩺 AI Medical Assistant (Mistral-7B)**  
An AI-powered chatbot that provides **medical assistance** using the **Mistral-7B-Instruct-v0.3** model via the Hugging Face API. Built using **Streamlit** for a simple and interactive user interface.  

---

## **📌 Features**
✅ **NLP-Powered Medical Chatbot** - Uses **Mistral-7B** for intelligent responses.  
✅ **Secure API Key Handling** - API key stored in `.env` file (ignored by Git).  
✅ **User-Friendly UI** - Built with **Streamlit** for smooth interaction.  
✅ **Fast and Accurate Responses** - Leverages the **Hugging Face API** efficiently.  

---

## **📦 Tech Stack**
| Technology      | Description |
|----------------|------------|
| **Python**     | Core programming language |
| **Streamlit**  | Web framework for building UI |
| **Requests**   | Makes API calls to Hugging Face |
| **dotenv**     | Loads API keys securely from `.env` |
| **Hugging Face API** | Provides access to the Mistral-7B model |

---

## **🚀 Installation Guide**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/PIYUSH-BHAVSAR/ai_chatbot_aicte.git
cd ai_chatbot_aicte
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up the API Key**
1. **Create a `.env` file** in the project directory.
2. **Add your Hugging Face API key** inside it:
   ```ini
   HUGGINGFACE_API_KEY="your_api_key_here"
   ```
3. **Ensure `.env` is added to `.gitignore`** to keep it private.

### **5️⃣ Run the Application**
```sh
streamlit run app.py
```

---

## **🛠 How It Works**
1. **Enter a medical question** in the input box.
2. **Click the "Ask" button** to submit your query.
3. The chatbot processes your input using **Mistral-7B** and returns a response.

---

## **📷 Screenshot**

![Description of Image](https://raw.githubusercontent.com/your-username/your-repo/main/Example_input_output/Screenshot 2025-02-10 214553.png)


---

## **📜 File Structure**
```
/ai_chatbot_aicte
│── .gitignore        # Ignore .env file
│── .env              # Stores API key (DO NOT SHARE)
│── requirements.txt  # List of dependencies
│── README.md         # Documentation
│── config.py         # Loads API key securely
│── app.py            # Streamlit application
```

---

## **📜 Environment Variables**
This project uses a `.env` file to store sensitive information.  
**Make sure `.env` is included in `.gitignore`** to prevent accidental exposure.

---

## **🐛 Troubleshooting**
| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'dotenv'` | Run `pip install python-dotenv` |
| `API Error: 401 (Unauthorized)` | Check if your API key is correct in `.env` |
| `ModuleNotFoundError: No module named 'streamlit'` | Run `pip install streamlit` |
| `Command not found: streamlit` | Ensure Streamlit is installed and activated in the virtual environment |

---

## **🤝 Contributing**
🎉 Want to improve this project? Feel free to fork, create an issue, or submit a pull request!  

---

## 🚀 Live Demo  
🖥️ Try the AI Medical Assistant here: [Health Assistant AICTE](https://health-assistant-aicte.streamlit.app/)
