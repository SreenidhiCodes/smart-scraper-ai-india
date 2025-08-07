{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPyMRdc9joOQWu/kdoJB0QX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SreenidhiCodes/smart-scraper-ai-india/blob/main/ai_india_scraper.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IZHUTfwaXDWX",
        "outputId": "697c73d5-08be-449c-c309-d56458c3077f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "24 AI-India related headlines saved to ai_in_india_headlines.txt\n"
          ]
        }
      ],
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "URL = \"https://www.analyticsindiamag.com/category/news/\"\n",
        "\n",
        "keywords = [\"AI\", \"Artificial Intelligence\", \"machine learning\", \"deep learning\", \"India\", \"Indian\"]\n",
        "\n",
        "\n",
        "response = requests.get(URL)\n",
        "if response.status_code != 200:\n",
        "    print(\"Failed to access the site.\")\n",
        "    exit()\n",
        "\n",
        "\n",
        "soup = BeautifulSoup(response.text, 'html.parser')\n",
        "\n",
        "headlines = []\n",
        "for tag in soup.find_all(['h2', 'h3']):\n",
        "    text = tag.get_text(strip=True)\n",
        "    if any(keyword.lower() in text.lower() for keyword in keywords):\n",
        "        headlines.append(text)\n",
        "\n",
        "headlines = list(set(headlines))\n",
        "\n",
        "\n",
        "with open(\"ai_in_india_headlines.txt\", \"w\", encoding=\"utf-8\") as f:\n",
        "    for line in headlines:\n",
        "        f.write(line + \"\\n\")\n",
        "\n",
        "print(f\"{len(headlines)} AI-India related headlines saved to ai_in_india_headlines.txt\")\n"
      ]
    }
  ]
}