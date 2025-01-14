# 🐞 Debugging FastAPI Application in VSCode

## Prerequisites

- Ensure you have [Visual Studio Code](https://code.visualstudio.com/) installed.
- Install the Python extension for VSCode, which provides support for Python development, including debugging.

## Steps to Debug

1. **Open the Project in VSCode:**

   - Launch VSCode and open your FastAPI project folder.

2. **Create a Debug Configuration:**

   - Click on the Run and Debug icon in the Activity Bar on the side of the window (or press `Ctrl+Shift+D`).
   - Click on "create a launch.json file" link.
   - Select "Python" as the environment.
   - Replace the contents of the `launch.json` file with the following configuration:

     ```json
     {
       "version": "0.2.0",
       "configurations": [
         {
           "name": "Python: FastAPI",
           "type": "python",
           "request": "launch",
           "program": "${workspaceFolder}/main.py",
           "console": "integratedTerminal",
           "args": ["run", "main:app", "--reload"],
           "jinja": true,
           "module": "uvicorn"
         }
       ]
     }
     ```

3. **Set Breakpoints:**

   - Open `main.py` or any other file you want to debug.
   - Click in the gutter to the left of the line numbers to set breakpoints.

4. **Start Debugging:**

   - Press `F5` or click the green play button in the Run and Debug view to start debugging.
   - The application will start, and VSCode will pause execution at any breakpoints you've set.

5. **Inspect Variables and Call Stack:**

   - Use the Debug panel to inspect variables, view the call stack, and control execution flow (step over, step into, continue, etc.).

6. **Stop Debugging:**

   - Click the red square stop button in the Debug toolbar to stop the debugging session.

## Additional Tips

- Ensure your virtual environment is activated in the VSCode terminal to use the correct Python interpreter.
- You can add more configurations to `launch.json` if needed, such as environment variables or different entry points.

By following these steps, you can effectively debug your FastAPI application using VSCode.
