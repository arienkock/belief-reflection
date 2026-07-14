import tools from "../tools.json";

type Tool = {
  id: string;
  title: string;
  path: string;
  status: "published" | "in-progress";
  summary: string;
};

const list = document.getElementById("tools-list")!;

for (const tool of tools as Tool[]) {
  const li = document.createElement("li");
  li.className = "tool-card";

  const link = document.createElement("a");
  link.href = import.meta.env.BASE_URL + tool.path;
  link.className = "tool-title";
  link.textContent = tool.title;

  const status = document.createElement("span");
  status.className = "tool-status tool-status-" + tool.status;
  status.textContent = tool.status === "published" ? "live" : "in progress";

  const summary = document.createElement("p");
  summary.className = "tool-summary";
  summary.textContent = tool.summary;

  const heading = document.createElement("div");
  heading.className = "tool-heading";
  heading.appendChild(link);
  heading.appendChild(status);

  li.appendChild(heading);
  li.appendChild(summary);
  list.appendChild(li);
}

if ((tools as Tool[]).length === 0) {
  list.innerHTML = "<li class=\"tool-empty\">No tools published yet.</li>";
}
