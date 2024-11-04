using Unity.VisualScripting;
using UnityEngine;

public class skrip : MonoBehaviour
{
    public Rigidbody2D myRigidbody;
    public float flapStrength;
    public LogicScript logic;
    public bool birdIsAlive = true;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {   
        gameObject.name = "borong";
        logic = GameObject.FindGameObjectWithTag("Logic").GetComponent<LogicScript>();

    }

    // Update is called once per frame
    void Update()
    {   
        
        if (Input.GetKeyDown(KeyCode.Space) && birdIsAlive )
        {
            myRigidbody.linearVelocity = new Vector2(0, 1) * flapStrength;
        }

        if (transform.position.y <= -8)
        {
            transform.position = new Vector2(0, -8);
            /*myRigidbody.gravityScale = 0;
            myRigidbody.mass = 0;*/
        }

    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        logic.gameOver();
        birdIsAlive = false;
    }
}
