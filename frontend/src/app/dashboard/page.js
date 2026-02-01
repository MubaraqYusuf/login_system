"use client";

export default function Dashboard() {
  function logout() {
    document.cookie = "access_token=; Max-Age=0";
    window.location.href = "/";
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-900">
      <div className="bg-gray-800 p-10 rounded-xl shadow-lg text-center">
        <h1 className="text-white text-3xl font-bold mb-4">
          🎉 Welcome!
        </h1>

        <p className="text-gray-300 mb-8">
          You are now logged in successfully.
        </p>

        <button
          onClick={logout}
          className="bg-red-600 hover:bg-red-700 px-6 py-3 rounded text-white font-semibold"
        >
          Logout
        </button>
      </div>
    </main>
  );
}
