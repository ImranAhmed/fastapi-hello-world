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

3. **⬆️ Download Latest Python Version:**

   - Go to the [official Python website](https://www.python.org/downloads/).
   - Download the latest Python installer for Windows.
   - **Run the Installer:**
     - Double-click the downloaded installer.
     - Make sure to check the box that says "Add Python to PATH" before clicking "Install Now."
   - **Verify the Installation:**

     - Open a new command prompt or terminal.
     - Run the following command to verify the installation:

       ```bash
       python --version
       ```

4. **⬆️ Upgrade `pip`:**

   Before installing dependencies, ensure `pip` is up to date:

   ```bash
   python -m pip install --upgrade pip
   ```

5. **📦 Install the dependencies:**

   If you encounter SSL certificate issues, you can use the `--trusted-host` option:

   ```bash
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
   ```

6. **🏃‍♂️ Run the FastAPI application:**

   ```bash
   uvicorn main:app --reload
   ```

7. **🌐 Access the application:**

   Open your browser and go to `http://127.0.0.1:8000` to see the "Hello, World!" message.

---

For more information on how to use FastAPI, visit the [official FastAPI documentation](https://fastapi.tiangolo.com/).

By following these steps, you can ensure that new developers use the correct Python version for your project.
