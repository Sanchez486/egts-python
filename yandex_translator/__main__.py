from . import translator


def main(*args):
    try:
        detailed_logging = "detailed_logging" in args
        translator_instance = translator.Translator(detailed_logging=detailed_logging)
        translator_instance.run()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
