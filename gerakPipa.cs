using UnityEngine;

public class skripPipa : MonoBehaviour
{
    public float moveSpeed = 5;
    private float deadZone = -20;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
        transform.position += (new Vector3(-1, 0, 0) * moveSpeed) * Time.deltaTime;
        
        if (transform.position.x < deadZone)
        {
            Destroy(gameObject);
        }
    }
}
