using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class LogicScript : MonoBehaviour
{
    public int playerScore;
    public Text scoreText;
    public GameObject gameOverScreen;
    public int naufal;

    [ContextMenu("Add Score")]
    public void addScore()
    {
        playerScore += 1;
        scoreText.text = playerScore.ToString();
    }

    public void restartGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);    
    }

    public void gameOver()
    {
        gameOverScreen.SetActive(true);
    }
}
