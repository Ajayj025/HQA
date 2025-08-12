# Heal Quick Agent

## Your Intelligent Healthcare Assistant

Heal Quick Agent is an AI-powered healthcare assistant designed to streamline health management by providing intelligent analysis and personalized support. Leveraging advanced language models, this agent helps users understand medical information, manage their health sessions, and interact with an intelligent system for medical inquiries.

---

## ✨ Features

* **Multi-Model Intelligence**: Utilizes a tiered system of Groq-powered AI models (Llama-4, Llama-3.3, Llama-3.1, Llama-3-70B) for robust and reliable analysis, with automatic fallback for enhanced resilience.
* **Secure User Authentication**: Features a complete authentication system using Supabase, allowing users to sign up, sign in, and manage their sessions securely.
* **Personalized Chat Sessions**: Users can create and manage individual chat sessions, each with a unique history for focused medical discussions.
* **Persistent Chat History**: All messages within a session are saved and retrieved from Supabase, ensuring continuity and comprehensive record-keeping.
* **Dynamic Model Management**: Intelligently selects the best available AI model for analysis, including retry mechanisms and rate limit handling.
* **Email Validation**: Ensures valid email formats during user registration.
* **Session Management**: Validates and manages user sessions, providing a seamless and secure experience.

---

## 🛠️ Technologies Used

* **Python**: Core programming language.
* **Streamlit**: For building the interactive web application interface.
* **Groq API**: Powers the intelligent language models for analysis.
* **Supabase**: Provides backend services for authentication and database management.
* **`st-supabase-connection`**: Streamlit component for easy Supabase integration.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* Git

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/heal-quick-agent.git](https://github.com/your-username/heal-quick-agent.git)
    cd heal-quick-agent
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(You'll need to create a `requirements.txt` file containing `groq`, `streamlit`, `st-supabase-connection`, etc. based on your project's exact dependencies.)*

### Supabase Setup

1.  **Create a Supabase project:**
    Go to [Supabase](https://supabase.com/) and create a new project.
2.  **Set up your database tables:**
    You'll need tables for `users`, `chat_sessions`, and `chat_messages` with appropriate schemas to match the `AuthService` logic.
    * **`users` table**:
        * `id` (UUID, Primary Key)
        * `email` (Text, Unique)
        * `name` (Text)
        * `created_at` (Timestamp with timezone, Default: `now()`)
    * **`chat_sessions` table**:
        * `id` (UUID, Primary Key, Default: `uuid_generate_v4()`)
        * `user_id` (UUID, Foreign Key to `users.id`)
        * `title` (Text)
        * `created_at` (Timestamp with timezone, Default: `now()`)
    * **`chat_messages` table**:
        * `id` (UUID, Primary Key, Default: `uuid_generate_v4()`)
        * `session_id` (UUID, Foreign Key to `chat_sessions.id`)
        * `content` (Text)
        * `role` (Text, e.g., 'user', 'assistant')
        * `created_at` (Timestamp with timezone, Default: `now()`)

3.  **Configure Environment Variables (Streamlit Secrets):**
    In your Streamlit application, you'll need to configure secrets. For local development, create a `.streamlit/secrets.toml` file in your project root:

    ```toml
    # .streamlit/secrets.toml
    SUPABASE_URL = "YOUR_SUPABASE_URL"
    SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"
    GROQ_API_KEY = "YOUR_GROQ_API_KEY"
    ```
    Replace `YOUR_SUPABASE_URL`, `YOUR_SUPABASE_ANON_KEY`, and `YOUR_GROQ_API_KEY` with your actual credentials. For deployment, use Streamlit Cloud's secrets management.

### Running the Application

```bash
streamlit run main.py


💡 Usage
Once the application is running, you can:

Sign Up / Sign In: Create a new account or log in with existing credentials.

Create New Sessions: Start fresh chat sessions for different health inquiries.

Chat with the AI Agent: Input your medical data or questions, and receive AI-generated analysis and responses.

Manage Sessions: View past sessions and continue conversations.

Delete Sessions: Remove unwanted chat histories.

🤝 Contributing
We welcome contributions! Please feel free to open issues or submit pull requests.

Fork the repository.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📞 Contact
Your Name / Your Organization - [Your Email/LinkedIn/GitHub Profile]

Project Link: [https://www.google.com/search?q=https://github.com/Ajayj025/heal-quick-agent]
