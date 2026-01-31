"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function ProfilePage() {
  const router = useRouter();
  const [user, setUser] = useState<string>("");

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return router.push("/login");

    fetch("http://127.0.0.1:8000/me", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => setUser(data.username))
      .catch(() => router.push("/login"));
  }, [router]);

  const logout = () => {
    localStorage.removeItem("token");
    router.push("/login");
  };

  const deleteAccount = async () => {
    if (!confirm("Delete your account permanently?")) return;

    const token = localStorage.getItem("token");

    await fetch("http://127.0.0.1:8000/delete", {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` },
    });

    logout();
  };

  return (
    <div className="min-h-screen bg-black text-white">
      <div className="flex justify-between items-center p-6 border-b border-zinc-800">
        <h2 className="text-xl font-bold">Dashboard</h2>
        <button
          onClick={logout}
          className="bg-zinc-800 px-4 py-2 rounded"
        >
          Logout
        </button>
      </div>

      <div className="flex items-center justify-center h-[70vh]">
        <div className="bg-zinc-900 p-10 rounded-xl text-center">
          <h1 className="text-3xl mb-2">
            Welcome, <span className="text-blue-400">{user}</span> 👋
          </h1>
          <p className="text-zinc-400">Logged in successfully.</p>
        </div>
      </div>

      <div className="flex justify-center pb-10">
        <button
          onClick={deleteAccount}
          className="bg-red-600 px-6 py-3 rounded hover:bg-red-500"
        >
          Delete Account
        </button>
      </div>
    </div>
  );
}
