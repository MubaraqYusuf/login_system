"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function ProfilePage() {
  const router = useRouter();

  const [username] = useState<string | null>(() => {
    if (typeof window !== "undefined") {
      return localStorage.getItem("username");
    }
    return null;
  });

  useEffect(() => {
    if (!username) {
      router.push("/login");
    }
  }, [username, router]);

  const handleLogout = () => {
    localStorage.removeItem("username");
    router.push("/login");
  };

  const handleDelete = async () => {
    if (!username) return;

    const confirmed = confirm(
      "Are you sure you want to delete your account? This cannot be undone."
    );

    if (!confirmed) return;

    await fetch(`http://127.0.0.1:8000/delete/${username}`, {
      method: "DELETE",
    });

    localStorage.removeItem("username");
    router.push("/register");
  };

  if (!username) return null;

  return (
    <div className="min-h-screen bg-zinc-950 text-white flex flex-col">
      {/* TOP BAR */}
      <header className="flex items-center justify-between px-6 py-4 border-b border-zinc-800">
        <h1 className="text-lg font-semibold">Dashboard</h1>

        <div className="flex gap-3">
          <button
            onClick={handleLogout}
            className="rounded-lg bg-zinc-800 px-4 py-2 text-sm hover:bg-zinc-700 transition"
          >
            Logout
          </button>

          <button
            onClick={handleDelete}
            className="rounded-lg bg-red-600 px-4 py-2 text-sm font-semibold hover:bg-red-500 transition"
          >
            Delete Account
          </button>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="flex flex-1 items-center justify-center">
        <div className="w-full max-w-md rounded-2xl bg-zinc-900 p-10 shadow-xl text-center">
          <h2 className="text-3xl font-bold mb-3">
            Welcome, <span className="text-blue-400">{username}</span> 👋
          </h2>
          <p className="text-zinc-400">
            You’re logged in successfully.
          </p>
        </div>
      </main>
    </div>
  );
}
