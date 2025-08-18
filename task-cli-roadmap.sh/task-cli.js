import fs, { stat } from "node:fs";
import path from "node:path";
import repl from "node:repl";
import os from "node:os";

repl.start({
    prompt: "task-cli ", eval: (cmd, context, filename, callback) => {
        cmd = cmd.trim();
        if (cmd === "exit") {
            callback(null, "Exiting task-cli...");
            return;
        }
        if (cmd === "help") {
            callback(null, "Available commands: exit, help, list, add <task>, remove <task_id>");
            return;
        }
        if (cmd.startsWith("add ")) {
            const task = cmd.slice(4).trim();
            const tasksFile = path.join(process.cwd(), "/tasks.json");
            console.log(tasksFile);
            // if (!task) {
            //     callback(new Error("Task cannot be empty."));
            //     return;
            // }
            let tasks = [];
            // if (fs.existsSync(tasksFile)) {
            //     tasks = JSON.parse(fs.readFileSync(tasksFile, "utf-8"));
            // }
            if (fs.existsSync(tasksFile) && fs.statSync(tasksFile).size > 0) {
                tasks = JSON.parse(fs.readFileSync(tasksFile, "utf-8"));
            }
            tasks.push({ id: tasks.length + 1, description: task, status: 'to-do', createdAt: new Date().toLocaleString(), updatedAt: new Date().toLocaleString() });
            fs.writeFileSync(tasksFile, JSON.stringify(tasks, null, 2));
            callback(null, `Task added: ${task}`);
            return;
        }
        if (cmd.startsWith("delete ")) {
            const id = parseInt(cmd.slice(7).trim(), 10);
            const tasksFile = path.join(process.cwd(), "/tasks.json");
            if (!fs.existsSync(tasksFile)) {
                callback(new Error("No tasks found."));
                return;
            }
            let tasks = JSON.parse(fs.readFileSync(tasksFile, "utf-8"));
            tasks = tasks.filter(task => task.id !== id);
            fs.writeFileSync(tasksFile, JSON.stringify(tasks, null, 2));
            callback(null, `Task with ID ${id} removed.`);
            return;
        }
        if (cmd.startsWith("mark-in-progress ")) {
            const id = parseInt(cmd.slice(17).trim(), 10);
            // console.log("index", id);

            const tasksFile = path.join(process.cwd(), "/tasks.json");
            if (!fs.existsSync(tasksFile)) {
                callback(new Error("No tasks found."));
                return;
            }
            let tasks = JSON.parse(fs.readFileSync(tasksFile, "utf-8"));
            const taskIndex = tasks.find(task => task.id === id);
            // console.log("task details", taskIndex);
            if (taskIndex === -1) {
                callback(new Error(`Task with ID ${id} not found.`));
                return;
            }
            // console.log("is this task ? ==> ", taskIndex['status']);
            taskIndex.status = 'in-progress';
            taskIndex.updatedAt = new Date().toLocaleString();
            fs.writeFileSync(tasksFile, JSON.stringify(tasks, null, 2));
        }
        if (cmd.startsWith("list ")) {
            // if (cmd === "list") {
            const status = (cmd.slice(5).trim() || "").toLowerCase();

            console.log("status ===> ", status)
            ;
            const tasksFile = path.join(process.cwd(), "/tasks.json");
            if (!fs.existsSync(tasksFile)) {
                callback(new Error("No tasks found."));
                return;
            }
            const tasks = JSON.parse(fs.readFileSync(tasksFile));
            // callback(null, tasks.map(task => `${task.id}: ${task.description}`));
            if (status && !["to-do", "in-progress", "done"].includes(status)) {
                callback(new Error("Invalid status. Use 'to-do', 'in-progress', or 'done'."));
                return;
            }
            if (status === "" || !status) {
                callback(null, tasks.map(task => `${task.id}: ${task.description} [${task.status}] (Created: ${task.createdAt}, Updated: ${task.updatedAt})`));
                return;
            }
            callback(null, tasks.filter(task => !status || task.status === status).map(task => `${task.id}: ${task.description} [${task.status}] (Created: ${task.createdAt}, Updated: ${task.updatedAt})`));
            return;
        }

        // callback(new Error(`Unknown command: ${cmd}`));
    }
}).on("exit", () => {
    // console.log("Exiting task-cli. Goodbye!");
    process.exit(0);
});

// This code implements a simple command-line interface (CLI) for managing tasks.
// It allows users to add, remove, and list tasks, and provides a REPL interface    
// for interaction. The tasks are stored in a JSON file in the user's home directory.
// The CLI supports commands like "add <task>", "remove <task_id>", "list", and "help".
// The "exit" command terminates the CLI session.
// The code uses Node.js built-in modules such as 'fs' for file operations, 'path' for
// handling file paths, 'repl' for creating a read-eval-print loop, and 'os' for accessing
// the user's home directory. The tasks are stored in a file named ".tasks.json" in the
// user's home directory, and the tasks are managed as an array of objects with an ID and   
// the task description. The CLI provides feedback to the user for each command executed,
// including error handling for unknown commands and operations on non-existent tasks.

export default repl;


/**
 * 
 * Uncaught SyntaxError: Unexpected end of JSON input
 * This error occurs when trying to parse an empty or malformed JSON file.
 * To fix this, ensure that the tasks file exists and contains valid JSON before reading it.
 * For example, you can check if the file is empty before parsing:
 * if (fs.existsSync(tasksFile) && fs.statSync(tasksFile).size > 0) {
 *     tasks = JSON.parse(fs.readFileSync(tasksFile, "utf-8"));
 * }
 * This will prevent the error by ensuring that the file is not empty before attempting to parse it.
 */