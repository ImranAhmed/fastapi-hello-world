# 🌟 fastapi-hello-world

## 🚀 Setup Instructions

1. **📥 Clone the repository:**

   ```bash
   git clone https://github.com/ImranAhmed/fastapi-hello-world
   cd fastapi-hello-world
   ```

2. **🔧 Create a virtual environment and activate it:**

   - **Using Command Prompt:**

     ```bash
     venv\Scripts\activate
     ```

   - **Using PowerShell:**

     ```bash
     .\venv\Scripts\Activate.ps1
     ```

     _Note: If you encounter an error regarding script execution policies, you may need to run PowerShell as an administrator and execute:_

     ```bash
     Set-ExecutionPolicy RemoteSigned
     ```

   - **Using Git Bash:**

     ```bash
     source venv/Scripts/activate
     ```

3. **⬆️ Upgrade `pip`:**

   Before installing dependencies, ensure `pip` is up to date:

   ```bash
   python -m pip install --upgrade pip
   ```

4. **📦 Install the dependencies:**

   If you encounter SSL certificate issues, you can use the `--trusted-host` option:

   ```bash
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
   ```

5. **🏃‍♂️ Run the FastAPI application:**

   ```bash
   uvicorn main:app --reload
   ```

6. **🌐 Access the application:**

   Open your browser and go to `http://127.0.0.1:8000` to see the "Hello, World!" message.
