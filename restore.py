import json
import os

transcript_path = r"C:\Users\bahsi\.gemini\antigravity-ide\brain\48bdb777-39d9-4079-b135-376528c1ed3a\.system_generated\logs\transcript.jsonl"
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = data.get("content", "")
        if "output" in content and "contact.html" in content and "Showing lines 1 to 609" in content:
            lines = content.split("\n")
            out_lines = []
            capturing = False
            for l in lines:
                if l.startswith("1: <!DOCTYPE html>"):
                    capturing = True
                if l.startswith("The above content shows the entire"):
                    capturing = False
                if capturing:
                    parts = l.split(": ", 1)
                    if len(parts) == 2 and parts[0].isdigit():
                        out_lines.append(parts[1])
                    else:
                        out_lines.append(l)
            if out_lines:
                with open("contact.html", "w", encoding='utf-8') as cf:
                    cf.write("\n".join(out_lines))
                    print("Restored contact.html")

        if "output" in content and "team.html" in content and "Showing lines 1 to 409" in content:
            lines = content.split("\n")
            out_lines = []
            capturing = False
            for l in lines:
                if l.startswith("1: <!DOCTYPE html>"):
                    capturing = True
                if l.startswith("The above content shows the entire"):
                    capturing = False
                if capturing:
                    parts = l.split(": ", 1)
                    if len(parts) == 2 and parts[0].isdigit():
                        out_lines.append(parts[1])
                    else:
                        out_lines.append(l)
            if out_lines:
                with open("team.html", "w", encoding='utf-8') as cf:
                    cf.write("\n".join(out_lines))
                    print("Restored team.html")

        if "output" in content and "vehicle.html" in content and "Showing lines 1 to 574" in content:
            lines = content.split("\n")
            out_lines = []
            capturing = False
            for l in lines:
                if l.startswith("1: <!DOCTYPE html>"):
                    capturing = True
                if l.startswith("The above content shows the entire"):
                    capturing = False
                if capturing:
                    parts = l.split(": ", 1)
                    if len(parts) == 2 and parts[0].isdigit():
                        out_lines.append(parts[1])
                    else:
                        out_lines.append(l)
            if out_lines:
                with open("vehicle.html", "w", encoding='utf-8') as cf:
                    cf.write("\n".join(out_lines))
                    print("Restored vehicle.html")
