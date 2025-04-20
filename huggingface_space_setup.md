# Setting Up Your Hugging Face Space

Follow these steps to create and set up your Hugging Face Space:

## 1. Create a Space on Hugging Face

1. Go to [https://huggingface.co/spaces](https://huggingface.co/spaces)
2. Click on "Create new Space"
3. Enter the following details:
   - Owner: fartec0
   - Space name: H4X0R-OMEGA-H1ST0RY
   - License: MIT
   - SDK: Gradio (or select the appropriate SDK for your application)
   - Space hardware: CPU (Free)
   - Visibility: Public

## 2. Add Your GitHub Token to the Space

1. Go to your Hugging Face profile settings
2. Navigate to "Access Tokens"
3. Create a new token with "write" access
4. Copy the token

## 3. Configure GitHub Secret for Automated Sync

1. Go to your GitHub repository
2. Navigate to Settings > Secrets and variables > Actions
3. Click on "New repository secret"
4. Add a new secret with:
   - Name: HF_TOKEN
   - Value: [Your Hugging Face token from step 2]

## 4. Initialize Your Space

Once you've created your Space, you'll need to push your code to it the first time:

```bash
git remote add huggingface https://huggingface.co/spaces/fartec0/H4X0R-OMEGA-H1ST0RY
git push -f huggingface main
```

## 5. Verify Deployment

After pushing your code:
1. Visit your Space URL: [https://huggingface.co/spaces/fartec0/H4X0R-OMEGA-H1ST0RY](https://huggingface.co/spaces/fartec0/H4X0R-OMEGA-H1ST0RY)
2. Wait for the build to complete (this may take a few minutes)
3. Your app should now be live and public! 