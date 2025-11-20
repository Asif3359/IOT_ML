# HuggingFace Authentication Setup

The BD Crop Disease Model repository is **gated**, which means you need to authenticate and request access to use it.

## Step-by-Step Setup

### 1. Create a HuggingFace Account

If you don't have one, create an account at:
👉 **https://huggingface.co/join**

### 2. Request Access to the Model

1. Go to the model repository:
   👉 **https://huggingface.co/Saon110/bd-crop-vegetable-plant-disease-model**

2. Click the **"Request access"** button
   - You may need to accept terms of use
   - Wait for approval (usually automatic or quick)

3. Once approved, you'll see "You have been granted access"

### 3. Generate a HuggingFace Token

1. Go to your HuggingFace settings:
   👉 **https://huggingface.co/settings/tokens**

2. Click **"New token"**

3. Choose:
   - **Name**: `bd-crop-disease-model` (or any name)
   - **Type**: **Read** (sufficient for downloading models)

4. Click **"Generate token"**

5. **Copy the token immediately** (you won't see it again!)

### 4. Set the Token as Environment Variable

#### Option A: Using `.env` file (Recommended)

Create or edit `.env` file in your project root:

```bash
# .env file
HF_TOKEN=your_token_here
# or
HUGGINGFACE_TOKEN=your_token_here
```

#### Option B: Export in Terminal (Temporary)

```bash
export HF_TOKEN='your_token_here'
# or
export HUGGINGFACE_TOKEN='your_token_here'
```

#### Option C: Add to Shell Profile (Permanent)

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export HF_TOKEN='your_token_here'
```

Then reload:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

### 5. Verify Setup

Run the test script to verify:

```bash
python test_direct.py
```

You should see:
```
✅ Authenticated with HuggingFace
📥 Downloading model weights...
✅ Model weights downloaded
```

## Troubleshooting

### Error: "401 Client Error - Unauthorized"

**Solution**: 
- Make sure you requested access to the repository
- Verify your token is correct
- Check that the token has "Read" permissions

### Error: "Cannot access gated repo"

**Solution**:
- Go to https://huggingface.co/Saon110/bd-crop-vegetable-plant-disease-model
- Click "Request access" if you haven't already
- Wait for approval (usually instant)

### Error: "Token not found"

**Solution**:
- Check that you set `HF_TOKEN` or `HUGGINGFACE_TOKEN` in your environment
- Verify the `.env` file is in the project root
- Make sure `python-dotenv` is installed: `pip install python-dotenv`

### Token Not Working?

1. Generate a new token at https://huggingface.co/settings/tokens
2. Delete the old one
3. Update your environment variable with the new token

## For Production/Deployment

When deploying to cloud services (Render, Heroku, etc.):

1. Add `HF_TOKEN` as an environment variable in your deployment dashboard
2. Set it to your HuggingFace token
3. The app will automatically use it

## Security Note

⚠️ **Never commit your token to git!**

- Add `.env` to `.gitignore` (already done)
- Don't hardcode tokens in code
- Use environment variables only

