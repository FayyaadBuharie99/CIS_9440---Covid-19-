{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "source": [
        "!pip install snowflake-connector-python pandas\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "slwzgJkLsOTG",
        "outputId": "9e6f8f0d-1379-4406-9f9a-89ae4dfc0e0f"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: snowflake-connector-python in /usr/local/lib/python3.10/dist-packages (3.10.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (2.0.3)\n",
            "Requirement already satisfied: asn1crypto<2.0.0,>0.24.0 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (1.5.1)\n",
            "Requirement already satisfied: cffi<2.0.0,>=1.9 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (1.16.0)\n",
            "Requirement already satisfied: cryptography<43.0.0,>=3.1.0 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (42.0.7)\n",
            "Requirement already satisfied: pyOpenSSL<25.0.0,>=16.2.0 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (24.1.0)\n",
            "Requirement already satisfied: pyjwt<3.0.0 in /usr/lib/python3/dist-packages (from snowflake-connector-python) (2.3.0)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (2023.4)\n",
            "Requirement already satisfied: requests<3.0.0 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (2.31.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (24.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (3.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (2024.2.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (4.11.0)\n",
            "Requirement already satisfied: filelock<4,>=3.5 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (3.14.0)\n",
            "Requirement already satisfied: sortedcontainers>=2.4.0 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (2.4.0)\n",
            "Requirement already satisfied: platformdirs<5.0.0,>=2.6.0 in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (4.2.1)\n",
            "Requirement already satisfied: tomlkit in /usr/local/lib/python3.10/dist-packages (from snowflake-connector-python) (0.12.5)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.1)\n",
            "Requirement already satisfied: numpy>=1.21.0 in /usr/local/lib/python3.10/dist-packages (from pandas) (1.25.2)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi<2.0.0,>=1.9->snowflake-connector-python) (2.22)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0->snowflake-connector-python) (2.0.7)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from snowflake.connector.pandas_tools import write_pandas\n",
        "import snowflake.connector"
      ],
      "metadata": {
        "id": "5FY2fEiYsTaJ"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Replace these with your Snowflake credentials and connection details\n",
        "snowflake_account = 'dgbtmhw-qz33201'\n",
        "snowflake_user = 'MBuharie99'\n",
        "snowflake_password = 'CISproject9088'\n",
        "snowflake_database = 'Aircraft_Noise'\n",
        "snowflake_schema = 'Aircraft_Data'\n",
        "snowflake_warehouse = 'COMPUTE_WH'"
      ],
      "metadata": {
        "id": "za1Gfp7WsYNl"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "conn = snowflake.connector.connect(\n",
        "    user=snowflake_user,\n",
        "    password=snowflake_password,\n",
        "    account=snowflake_account,\n",
        "    warehouse=snowflake_warehouse,\n",
        "    database=snowflake_database,\n",
        "    schema=snowflake_schema\n",
        ")\n"
      ],
      "metadata": {
        "id": "IhciilaysnCt"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "json_file_path = '/content/output_all.json'\n",
        "df = pd.read_json(json_file_path)"
      ],
      "metadata": {
        "id": "UjhXT_uEssEV"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns = df.columns.str.replace('\"', '')"
      ],
      "metadata": {
        "id": "N5aoz38xtusN"
      },
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "write_pandas(conn, df, 'YOUR_TABLE_NAME')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T7beH_MXs8Tg",
        "outputId": "4a2bc606-534c-49aa-ad30-719838cf3e69"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(True,\n",
              " 1,\n",
              " 7615,\n",
              " [('cxmdmlnqrg/file0.txt',\n",
              "   'LOADED',\n",
              "   7615,\n",
              "   7615,\n",
              "   1,\n",
              "   0,\n",
              "   None,\n",
              "   None,\n",
              "   None,\n",
              "   None)])"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    }
  ]
}