{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMrjS8oORHsQoTFDVVGRHW6",
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
        "<a href=\"https://colab.research.google.com/github/omar-mostafa-taha/Tic-Tac-Toe/blob/main/Omar_Mostafa_Tic_Tac_Toe_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Rc3jjwKjC9ni"
      },
      "outputs": [],
      "source": [
        "def create_board():\n",
        "  board=[[1,2,3],[4,5,6],[7,8,9]]\n",
        "  return board\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def show_board(board):\n",
        "  for i in board:\n",
        "    for j in i:\n",
        "      print(j,end='\\t')\n",
        "    print('\\n')"
      ],
      "metadata": {
        "id": "qbljnXnnGwtQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def player_choice(choice,x_o,board):   #return 1 if succeeded 0 otherwise\n",
        "    for i in [0,1,2]:\n",
        "      for j in [0,1,2]:\n",
        "          if (board[i][j] == choice) and (board[i][j] not in ['X','O']):\n",
        "                board[i][j]=x_o\n",
        "                return 1\n",
        "    print(\"invalid position\")\n",
        "    return 0\n",
        "              "
      ],
      "metadata": {
        "id": "V6Eojr7wII40"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def check_win(board):\n",
        "  \n",
        "    for i in board:     #check horizontal\n",
        "      if i[0]==i[1] and i[1]==i[2]:\n",
        "        print(\"player {} won!\".format(i[0]))\n",
        "        return True\n",
        "\n",
        "    for i in [0,1,2]:   #check vertical\n",
        "        if board[0][i]== board[1][i] and board[1][i]==board[2][i]:\n",
        "          print(\"player {} won!\".format(board[0][i]))\n",
        "          return True\n",
        "\n",
        "    if (board[0][0]==board[1][1] == board[2][2]) or (board[0][2]==board[1][1]==board[2][0]): #check diagonal\n",
        "      print(\"player {} won!\".format(board[1][1]))\n",
        "      return True\n",
        "    else:\n",
        "      return False\n",
        "      \n"
      ],
      "metadata": {
        "id": "RARdH_5sKVb9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def check_draw(board):\n",
        "  for i in [0,1,2]:\n",
        "    for j in [0,1,2]:\n",
        "      if board[i][j] not in [\"X\",\"O\"]:\n",
        "        return False \n",
        "  print(\"The game is Draw!\")\n",
        "  return True"
      ],
      "metadata": {
        "id": "1qP1GDIQMfQQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def play_game():\n",
        "  board=create_board()\n",
        "  show_board(board)\n",
        "  i=0   \n",
        "  game_end = check_draw(board) or check_win(board)\n",
        "  while not game_end:\n",
        "    \n",
        "    if i%2==0:      #player X turn\n",
        "      pos=int(input(\"player X turn\\nPlease Enter a number between 1,9 represents an empty position:\"))\n",
        "      success=player_choice(pos,\"X\",board)\n",
        "      if not success:\n",
        "        continue\n",
        "        \n",
        "\n",
        "    else:     #player O turn\n",
        "      pos=int(input(\"player O turn\\nPlease Enter a number between 1,9 represents an empty position:\"))\n",
        "      success=player_choice(pos,\"O\",board)\n",
        "      if not success:\n",
        "        continue\n",
        "    show_board(board)\n",
        "    game_end = check_draw(board) or check_win(board)\n",
        "    i+=1"
      ],
      "metadata": {
        "id": "xV1MwLKtiOVd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  print(\"\\t\\tWelcome\\n\")\n",
        "  play=input(\"to start the game press y: \")\n",
        "  while play=='y':\n",
        "    play_game()\n",
        "    play=input(\"to keep playing press y: \")\n",
        "  print(\"\\t\\tThanks!\")"
      ],
      "metadata": {
        "id": "Mr1hWQySjrVQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EeSF52qMqQ6h",
        "outputId": "2429db45-73b1-44bc-c526-5673d10f1995"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\t\tWelcome\n",
            "\n",
            "to start the game press y: y\n",
            "1\t2\t3\t\n",
            "\n",
            "4\t5\t6\t\n",
            "\n",
            "7\t8\t9\t\n",
            "\n",
            "player X turn\n",
            "Please Enter a number between 1,9 represents an empty position:1\n",
            "X\t2\t3\t\n",
            "\n",
            "4\t5\t6\t\n",
            "\n",
            "7\t8\t9\t\n",
            "\n",
            "player O turn\n",
            "Please Enter a number between 1,9 represents an empty position:6\n",
            "X\t2\t3\t\n",
            "\n",
            "4\t5\tO\t\n",
            "\n",
            "7\t8\t9\t\n",
            "\n",
            "player X turn\n",
            "Please Enter a number between 1,9 represents an empty position:3\n",
            "X\t2\tX\t\n",
            "\n",
            "4\t5\tO\t\n",
            "\n",
            "7\t8\t9\t\n",
            "\n",
            "player O turn\n",
            "Please Enter a number between 1,9 represents an empty position:2\n",
            "X\tO\tX\t\n",
            "\n",
            "4\t5\tO\t\n",
            "\n",
            "7\t8\t9\t\n",
            "\n",
            "player X turn\n",
            "Please Enter a number between 1,9 represents an empty position:5\n",
            "X\tO\tX\t\n",
            "\n",
            "4\tX\tO\t\n",
            "\n",
            "7\t8\t9\t\n",
            "\n",
            "player O turn\n",
            "Please Enter a number between 1,9 represents an empty position:9\n",
            "X\tO\tX\t\n",
            "\n",
            "4\tX\tO\t\n",
            "\n",
            "7\t8\tO\t\n",
            "\n",
            "player X turn\n",
            "Please Enter a number between 1,9 represents an empty position:7\n",
            "X\tO\tX\t\n",
            "\n",
            "4\tX\tO\t\n",
            "\n",
            "X\t8\tO\t\n",
            "\n",
            "player X won!\n",
            "to keep playing press y: h\n",
            "\t\tThanks!\n"
          ]
        }
      ]
    }
  ]
}