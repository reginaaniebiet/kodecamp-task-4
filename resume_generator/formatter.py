def format_resume(data):
    lines = []

    # Header
    lines.append(f"{data['name'].upper()} - {data['title']}\n")
    lines.append(f"📧 {data['contact']['email']} | 📞 {data['contact']['phone']} | 📍 {data['contact']['address']}\n")

    # Summary
    lines.append("🔹 SUMMARY")
    lines.append(data['summary'] + "\n")

    # Skills
    lines.append("🔹 SKILLS")
    lines.append(", ".join(data['skills']) + "\n")

    # Education
    lines.append("🔹 EDUCATION")
    for edu in data['education']:
        lines.append(f"{edu['degree']} - {edu['institution']} ({edu['year']})")

    # Experience
    lines.append("\n🔹 EXPERIENCE")
    for exp in data['experience']:
        lines.append(f"{exp['role']} at {exp['company']} ({exp['duration']})")
        lines.append(f"  - {exp['description']}")

    return "\n".join(lines)
