Remove Course Operators persona
###############################

Status
******

**Accepted**

Context
*******

As documented in :doc:`0001-purpose-of-this-repo`, we list out a number of
target personas for whom to create documentation; one of these is the "course
operator" persona, defined as those who run an Open edX course.

In practice, we have not developed documentation for this persona. We have found
that there is a very blurry line between someone who authors a course (an
"Educator") and someone who runs one. As such, documentation about how to
utilize a given feature frequently combines the needs of an educator and a
course operator into one document.

Decision
********

We will no longer have the persona of "Course Operator". This was discussed in
multiple Documentation Working Group meetings in August and September of 2024.

All documentation related to building/authoring a course, running a course, and
utilizing all "course personell"-type software (including but not limited to
Studio, the LMS Instructor Dashboard, the Staff Debug interface, and Aspects)
will lie under the "Educator" persona.

Consequences
************

* All pages for Course Operators will be deleted. There was never any authored
  content on these pages; they were just stubs.
