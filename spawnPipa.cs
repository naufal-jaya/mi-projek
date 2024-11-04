using UnityEngine;

public class spawnPipa : MonoBehaviour
{
    public GameObject pipe;
    public float spawnRate = 2;
    public float timer = -100;
    public float extremeHeightOffset = 10;


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        if (timer < spawnRate)
        {
            timer += Time.deltaTime;
        } else
        {
            SpawnPipa();
            timer = 0;
        }
    }

    void SpawnPipa()
    {
        float maxHeight = transform.position.y + extremeHeightOffset;
        float minHeight = transform.position.y - extremeHeightOffset; 

        Instantiate(pipe, new Vector3(transform.position.x, Random.Range(minHeight, maxHeight), transform.position.z), transform.rotation);
        /*Instantiate(pipe, transform.position, transform.rotation);*/
    }
}
