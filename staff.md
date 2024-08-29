---
layout: page
title: Staff
nav_order: 7
description: A listing of all the course staff members.
---

# Staff

Append `@berkeley.edu` to all email addresses. **For personal circumstances or sensitive matters,** please use the staff email address **[data102@berkeley.edu](mailto:data102@berkeley.edu)**, which is monitored only by the instructors and a few lead TAs.

**Note:** Consult the [calendar]({{site.baseurl}}/calendar) for the most up-to-date office hours.

{% assign professors = site.staffers | where: 'role', 'Professor' | reverse %}
{% assign num_professors = professors | size %}
{% if num_professors != 0 %}
## Professors

<div class = "role flex">
    {% for staffer in professors %}
    {{ staffer }}
    {% endfor %}
</div>
{% endif %}
    
{% assign instructors = site.staffers | where: 'role', 'Instructor' | reverse %}
{% assign num_instructors = instructors | size %}
{% if num_instructors != 0 %}
## Instructors

{% for staffer in instructors %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign staff = site.staffers | where: 'team', 'Staff' | reverse %}
{% assign num_staff = staff | size %}
{% if num_staff != 0 %}
## Course Staff

<div class = "role flex">
    {% for staffer in staff %}
    {{ staffer }}
    {% endfor %}
</div>
{% endif %}
