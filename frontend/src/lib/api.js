const API_URL = "http://127.0.0.1:8000";

export async function register(username, password) {
  const res = await fetch(`${API_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  return res.json();
}

export async function login(username, password) {
  const res = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ username, password }),
  });
  return res.json();
}

export async function deleteUser(username) {
  const res = await fetch(`${API_URL}/delete/${username}`, {
    method: "DELETE",
    credentials: "include",
  });
  return res.json();
}
