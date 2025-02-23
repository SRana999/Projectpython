def main():
    news_articles = []

    while True:
        print("\n===== Fact-Checking Newspaper =====")
        print("1. Add News Article")
        print("2. Show All News")
        print("3. Verify News (Source, Image/Video, Text)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            news = input("Enter the news article: ")
            news_articles.append({"news": news, "verified": False, "status": "Unverified"})
            print("News added!")

        elif choice == '2':
            print("\nNews Articles:")
            for index, article in enumerate(news_articles):
                print(f"{index + 1}. {article['news']} - Status: {article['status']}")

        elif choice == '3':
            if not news_articles:
                print("No news to verify.")
                continue

            news_index = int(input("Enter the news number to verify: ")) - 1
            if 0 <= news_index < len(news_articles):
                print("Choose verification method:")
                print("1. Source Verification")
                print("2. Image/Video Analysis")
                print("3. Text Analysis")

                method = input("Enter method number: ")

                if method == '1':
                    source = input("Enter source name: ")
                    if source.lower() in ["bbc", "reuters", "ap", "the guardian"]:
                        news_articles[news_index]["verified"] = True
                        news_articles[news_index]["status"] = "Verified by Source"
                    else:
                        news_articles[news_index]["status"] = "Unreliable Source"

                elif method == '2':
                    image_check = input("Does the image/video appear in multiple sources? (yes/no): ")
                    if image_check.lower() == "yes":
                        news_articles[news_index]["verified"] = True
                        news_articles[news_index]["status"] = "Verified by Image/Video"
                    else:
                        news_articles[news_index]["status"] = "Potentially Fake Media"

                elif method == '3':
                    text_check = input("Does the text match credible sources? (yes/no): ")
                    if text_check.lower() == "yes":
                        news_articles[news_index]["verified"] = True
                        news_articles[news_index]["status"] = "Verified by Text"
                    else:
                        news_articles[news_index]["status"] = "Possible Fake News"

                else:
                    print("Invalid method.")
                    continue

                print("News verification updated!")
            else:
                print("Invalid news number.")

        elif choice == '4':
            print("Exiting Fact-Checking Newspaper.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
