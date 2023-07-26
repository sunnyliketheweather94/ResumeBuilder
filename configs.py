import configparser as cp 


if __name__ == '__main__':
    config = cp.ConfigParser()

    config['OpenAI'] = {
        'organization' : 'ORGANIZATION',
        'api_key' : 'API_KEY'
    }

    with open('.configs.ini', 'w') as f:
        config.write(f)