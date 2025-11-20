# Quick Start Guide - HuggingFace Authentication

## The Problem

The model repository `Saon110/bd-crop-vegetable-plant-disease-model` is **gated**, meaning:
- You need a HuggingFace account
- You must request access to the repository
- You need an authentication token to download the model

## Quick Fix (3 Steps)

### 1. Request Access (2 minutes)

Go to: **https://huggingface.co/Saon110/bd-crop-vegetable-plant-disease-model**

Click **"Request access"** and accept terms.

### 2. Get Your Token (1 minute)

1. Go to: **https://huggingface.co/settings/tokens**
2. Click **"New token"**
3. Name it (e.g., `bd-crop-model`)
4. Select **"Read"** type
5. Click **"Generate"**
6. **Copy the token** (starts with `hf_...`)

### 3. Set the Token

**Option A: Create `.env` file** (Recommended)

```bash
# In your project root, create .env file:
echo "HF_TOKEN=your_token_here" > .env
```

**Option B: Export in terminal**

```bash
export HF_TOKEN='your_token_here'
```

**Option C: Add to shell profile** (Permanent)

```bash
echo 'export HF_TOKEN="your_token_here"' >> ~/.bashrc
source ~/.bashrc
```

## Test It

```bash
python test_direct.py
```

You should see:
```
✅ Authenticated with HuggingFace
📥 Downloading model weights...
✅ Model weights downloaded
```

## Run Your API

```bash
python app.py
```

The model will download automatically on first use!

## Need More Help?

See `HUGGINGFACE_SETUP.md` for detailed instructions.

