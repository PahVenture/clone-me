# CursorAI Integration Guide for clone-me

This guide explains how to integrate and use your clone-me repository with CursorAI, enhancing your coding experience with personalized knowledge and expertise.

## Setup

1. In your project's root directory, add the clone-me repository as a submodule:
   ```
   git submodule add git@github.com:udecode/dotai.git .clone-me
   ```
2. This creates a `.clone-me` folder containing your knowledge base.

## Usage with CursorAI

Once set up, CursorAI can access and utilize the information in your `.clone-me` folder. Here's how you can leverage this integration:

1. **Contextual Assistance**: CursorAI can now provide suggestions and insights based on your personal knowledge base while you're coding.

2. **Quick Reference**: Access your documented methodologies, best practices, and code snippets directly within your coding environment.

3. **Personalized Coding Style**: CursorAI can adapt its suggestions to match your preferred coding style and practices as documented in your clone-me repository.

4. **Project-Specific Knowledge**: If you include project-specific information in your clone-me repo, CursorAI can provide more relevant assistance for each project.

## Best Practices

1. **Keep It Updated**: Regularly update your clone-me repository to ensure CursorAI has access to your latest knowledge and preferences.

2. **Organize Well**: Maintain a clear structure in your clone-me repo for easier access by CursorAI.

3. **Use Tags**: Implement a tagging system in your markdown files to help CursorAI quickly locate relevant information.

4. **Include Code Snippets**: Add commonly used code snippets or patterns to your repo for quick insertion via CursorAI.

## Troubleshooting

If CursorAI isn't accessing your clone-me content:

1. Ensure the submodule was added correctly.
2. Check that the `.clone-me` folder is in the correct location.
3. Verify that CursorAI has the necessary permissions to access the folder.

By integrating your clone-me repository with CursorAI, you create a powerful, personalized coding assistant that understands and applies your unique knowledge and preferences.