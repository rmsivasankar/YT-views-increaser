from core.simulator import ViewSimulator
import sys

def main():
    print("YouTube View Simulator (Educational Purposes Only)")
    print("------------------------------------------------")
    print("WARNING: Using this violates YouTube's Terms of Service\n")
    
    simulator = ViewSimulator()
    
    # Get video URL
    while True:
        video_url = input("Enter YouTube video URL: ").strip()
        if simulator.validate_youtube_url(video_url):
            break
        print("Invalid URL. Example: https://www.youtube.com/watch?v=...")
    
    # Get view count
    while True:
        try:
            view_count = int(input(f"How many views to simulate? (1-{simulator.settings['max_views_per_run']} recommended): "))
            if 1 <= view_count <= simulator.settings['max_views_per_run']:
                break
            print(f"Please enter a number between 1 and {simulator.settings['max_views_per_run']}")
        except ValueError:
            print("Please enter a valid number")
    
    # Confirm
    confirm = input(f"\nAbout to simulate {view_count} views for {video_url}\n"
                   "This is for educational purposes only. Continue? (y/n): ").lower()
    if confirm != 'y':
        print("Cancelled")
        sys.exit()
    
    # Run simulation
    print("\nStarting simulation...\n")
    try:
        simulator.simulate_view(video_url, view_count)
        print("\nSimulation complete. Remember that artificial view inflation violates YouTube's Terms of Service.")
    except Exception as e:
        print(f"\nSimulation failed: {str(e)}")

if __name__ == "__main__":
    main()