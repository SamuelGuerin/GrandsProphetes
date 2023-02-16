import pathlib
import sys
workingDirectory = pathlib.Path().resolve()
sys.path.append(str(workingDirectory) + '\\Application\\UI')
from Form import Form

if __name__ == '__main__':
    app = Form()
    app.mainloop()