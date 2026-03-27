(Enable XQueue)=

# Enable and Test Event Bus–Based XQueue Submissions

```{tags}
site operator, reference
```

This guide explains how to enable and test **event bus–based XQueue submissions** in `openedx-platform`.
It is written for Open edX contributors and operators who want to validate event-driven external grading on the `master` branch.

```{contents} Contents
:depth: 1
:local:
```

## Architecture Overview

With event bus enabled, submission flow changes from direct polling to event-driven routing:

Learner Submission

→ LMS stores submission

→ LMS publishes submission event

→ Event bus distributes event

→ XQueue worker / watcher consumes event

→ Watcher posts result via edx-submissions API

→ LMS updates grade

The watcher authenticates using a Django superuser that must belong to the `xqueue` group.

---

## Prerequisites

* Local clone of `openedx-platform` (master branch recommended)
* Custom watcher script (e.g., {ref}`XQueue Custom Watcher`)
* Django superuser account
* Superuser added to group named `xqueue`
* Event bus enabled in LMS settings
* edx-submissions service available

---

## Environment Setup

### Option A (Using Tutor (Recommended Modern Setup))

Repository reference: [https://github.com/overhangio/tutor](https://github.com/overhangio/tutor)

### Step 1. Install Tutor

```bash
pip install tutor
```

Initialize:

```bash
tutor local quickstart
```

Start platform:

```bash
tutor local start
```

---

### Step 2. Create Superuser

```bash
tutor local run lms ./manage.py createsuperuser
```

---

### Step 3. Create `xqueue` Group

```bash
tutor local run lms ./manage.py shell
```

Then:

```python
from django.contrib.auth.models import Group
Group.objects.get_or_create(name="xqueue")
```

Add user to group:

```python
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username="your_username")
user.groups.add(Group.objects.get(name="xqueue"))
```

---

### Step 4. Ensure Event Bus is Running

Tutor uses Redis by default.

Verify:

```bash
tutor local ps
```

Redis should be listed.

---

### Step 5. Enable XQueue Event Bus Waffle Flag

Open LMS admin:

```
http://localhost:8000/admin
```

Go to:

Waffle → Flags

Create flag:

Name: `enable_xqueue_event_bus`

Active: True

Rollout: 100

Optional: course override via Waffle → Overrides.

---

### Option B (Using Deprecated Legacy Devstack)

Repository reference: [https://github.com/edx/devstack](https://github.com/edx/devstack)

### Step 1. Clone and Start Devstack

```bash
git clone https://github.com/edx/devstack.git
cd devstack
make dev.up
```

This brings up LMS, CMS, MySQL, Mongo, Redis, etc.

To rebuild after changes:

```bash
make dev.build
make dev.up
```

---

### Step 2. Create Superuser

```bash
make lms-shell
```

Inside container:

```bash
./manage.py createsuperuser
```

---

### Step 3. Create `xqueue` Group

Inside LMS shell:

```python
from django.contrib.auth.models import Group
Group.objects.get_or_create(name="xqueue")
```

Add superuser to group:

```python
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username="your_username")
user.groups.add(Group.objects.get(name="xqueue"))
```

---

### Step 4. Enable Event Bus

Ensure Redis container is running:

```bash
docker ps | grep redis
```

If needed:

```bash
make dev.up
```

Confirm event bus settings in LMS environment file.

---

## Create Advanced `code_response` Problem

In Studio, add Advanced problem with:

```xml
<problem display_name="XQueue Event Bus Test Problem">
  <response
      response_type="code_response"
      label="Enter any code"
      language="python"
      max_attempts="5"
      grader="xqueue">
  </response>
</problem>
```

Ensure:

* `grader="xqueue"`
* The course is published

---

## Running the Custom Watcher

Ensure credentials inside watcher:

```python
LMS_URL = "http://localhost:8000"
USERNAME = "admin"
PASSWORD = "password"
```

Run:

```bash
python custom_watcher.py
```

Expected output:

Connected to LMS
Polling for jobs
Graded submission with score = 1

---

## Submit as Learner

1. Log in as learner
2. Open problem
3. Submit response
4. Wait a few seconds

You should see score update automatically.

---

## Verification and Debugging

### Check Submissions in Django Shell

```python
from submissions.models import Submission
Submission.objects.all()
```

### Check Logs

Tutor:

```bash
tutor local logs lms
```

Legacy Devstack:

```bash
docker logs lms
```

### Common Issues

403 Forbidden → User not in xqueue group

No grading → Watcher not running

No event → Waffle flag disabled

Auth failure → Wrong credentials

---

## Final Checklist

* Tutor (or Devstack) running
* Superuser created
* xqueue group exists
* User added to xqueue group
* Waffle flag enabled
* Advanced problem created
* Watcher running
* Submission graded successfully

---

```{seealso}
{ref}`XQueue Reference` (reference)

{ref}`About External Grader Problems` (concept)

{ref}`Add an External Grader Problem` (how-to)
```

**Maintenance Chart**

| Review Date | Working Group Reviewer | Release | Test Situation |
|-------------|------------------------|---------|----------------|
| 2025-03-25  | Usama S                |Verawood | Pass           |
