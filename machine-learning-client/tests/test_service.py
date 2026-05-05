from service import build_prompt

def test_build_prompt_includes_assignment_fields():
    prompt = build_prompt(
        title="Final Project",
        course="Software Engineering",
        description="Finish CI/CD pipeline",
        due_date="2026-05-05",
        college="NYU",
        major="Computer Science",
        year="3",
    )

    assert "Final Project" in prompt
    assert "Software Engineering" in prompt
    assert "Finish CI/CD pipeline" in prompt
    assert "2026-05-05" in prompt
    assert "NYU" in prompt
    assert "Computer Science" in prompt
    assert "3" in prompt
    assert "difficulty" in prompt
    assert "priority" in prompt
    assert "estimated_hours" in prompt