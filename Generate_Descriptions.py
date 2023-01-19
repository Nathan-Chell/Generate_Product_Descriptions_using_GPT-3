import settings
import openai




def get_response(model, temperature, max_tokens, text):

    return openai.Completion.create(model=model, prompt=text, max_tokens=max_tokens, temperature=temperature)

def write_output(data, model):
    """Write output to file

    Args:
        data (String): Product description 
        model (String): Model used to generate the product description
    """

    with open("./data/{}_output.txt".format(model), "a") as f:
        f.write(data)

def main():


    #complex model creates a long description of about 3 sentences, small creates only one.
    openai.api_key = settings.Open_AI_Key
    complex_model = "text-davinci-003"
    small_model = "text-curie-001"
    temperature = 0.7
    max_tokens = 512

    #smaple input
    int_prompt = "Write a long product description for this item just use information from the points:"
    product_text = "This product comes with a free one year manufacturer guarantee. A free second year guarantee is available upon registering product. Dimensions (cm) - H142.0 x W55.0 x D55.0. 55 cm wide, 142 cm tall larder fridge with 230 litre net capacity. No freezer, 40dB noise level, 4 fixed door racks, 4 adjustable glass shelves, 1 storage compartment. RH55LF142SS"


    response = get_response(small_model, temperature, max_tokens, int_prompt+product_text)
    write_output(dict(response)['choices'][0]['text'], dict(response)['model'])

    response = get_response(complex_model, temperature, max_tokens, int_prompt+product_text)
    write_output(dict(response)['choices'][0]['text'], dict(response)['model'])

if __name__ == '__main__':
    main()
