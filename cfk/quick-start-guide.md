---
permalink: /get/how-to-contribute-quick-start-guide/
title: "How to contribute quick start guide"
layout: single
toc: false
author_profile: false
classes: wide
share: true
sidebar:
  nav: "get"
---

If you have browsed the site, you will have understood that the goal is to gather quality knowledge so that it is freely accessible. To achieve this goal, it is necessary to build a community that contributes with:
- contents such as books, courses, tutorials, and so on
- reviews of such contents
- definition of learning paths based on the contents.

This page describes how you can actively contribute. It is largely based on [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/) tutorial.

## Before acting
So, you have an idea but before doing anything, do a quick check to make sure it hasn’t been discussed elsewhere or someone is working on something similar. Skim the project’s [README](https://github.com/CFKNow/cfknow.github.io), [issues}(https://github.com/CFKNow/cfknow.github.io/issues) (open and closed), [community Discord server](https://cfknow.github.io/community/). You don’t have to spend hours going through everything, but a quick search for a few key terms goes a long way.

If you can’t find your idea elsewhere, you’re ready to make a move and you’ll likely communicate by doing the following:
- Raising an issue: these are like starting a conversation or discussion.
- Pull requests are for starting work on a solution.
- Community Discord server: Consider starting a conversation or asking for clarification about your contribution selecting the right channel.

Before you open an issue or pull request, check the project’s contributing docs [CONTRIBUTING](https://github.com/CFKNow/cfknow.github.io/blob/master/CONTRIBUTING.md), to see whether you need to include anything specific. 

If you want to make a substantial contribution, open an issue to ask before working on it. It’s helpful to watch the project for a while (on GitHub, you can click “Watch” to be notified of all conversations), and get to know community members, before doing work that might not get accepted.

## Opening an issue
You should usually open an issue in the following situations:
- Report an error you can’t solve yourself.
- Discuss a high-level topic or idea (for example, community, vision or policies).
- Propose a new feature or other project idea.

Tips for communicating on issues:
- If you see an open issue that you want to tackle, comment on the issue to let people know you’re on it. That way, people are less likely to duplicate your work.
- If an issue was opened a while ago, it’s possible that it’s being addressed somewhere else, or has already been resolved, so comment to ask for confirmation before starting work.
- If you opened an issue, but figured out the answer later on your own, comment on the issue to let people know, then close the issue. Even documenting that outcome is a contribution to the project.

## Opening a pull request
You should usually open a pull request in the following situations:
- Submit small fixes such as a typo, a broken link or an obvious error.
- Start work on a contribution that was already asked for, or that you’ve already discussed, in an issue.
- A pull request doesn’t have to represent finished work. It’s usually better to open a pull request early on, so others can watch or give feedback on your progress. Just open it as a “draft” or mark as a “WIP” (Work in Progress) in the subject line or “Notes to Reviewers” sections if provided. You can always add more commits later.

Here’s how to submit a pull request:
- [Fork the repository](https://guides.github.com/activities/forking/) and clone it locally. Connect your local to the original “upstream” repository by adding it as a remote. Pull in changes from “upstream” often so that you stay up to date so that when you submit your pull request, merge conflicts will be less likely. (See more detailed instructions here.)
- [Create a branch](https://guides.github.com/introduction/flow/) for your edits.
Reference any relevant issues or supporting documentation in your PR (for example, “Closes #37.”)
- Include screenshots of the before and after if your changes include differences in HTML/CSS. Drag and drop the images into the body of your pull request.
- Test your changes! Run your changes against any existing tests if they exist and create new ones when needed. It’s important to make sure your changes don’t break the existing project.
- Contribute in the style of the project to the best of your abilities. This may mean using indents, semi-colons or comments differently than you would in your own repository, but makes it easier for the maintainer to merge, others to understand and maintain in the future.

If this is your first pull request, check out [Make a Pull Request](https://makeapullrequest.com/), which Kent C. Dodds created as a walkthrough video tutorial. You can also practice making a pull request in the [First Contributions](https://github.com/firstcontributions/first-contributions) repository, created by Roshan Jossy.