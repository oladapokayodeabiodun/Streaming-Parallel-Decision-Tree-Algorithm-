from spdt import hello_world 

def test_hello_world():
    output_text = hello_world()
    expected_ouput = "Hello World"

    assert output_text == expected_ouput