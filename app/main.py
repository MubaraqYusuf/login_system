from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "admin" and password == "admin":
        return HTMLResponse("""
            <h2 style="text-align:center;">Login Successful 🎉</h2>
            <p style="text-align:center;">Welcome, admin!</p>
            <div style="text-align:center;">
                <a href="/">Logout</a>
            </div>
        """)

    return HTMLResponse("""
        <h2 style="text-align:center;color:red;">Invalid Login ❌</h2>
        <div style="text-align:center;">
            <a href="/">Try Again</a>
        </div>
    """)
