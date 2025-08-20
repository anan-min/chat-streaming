from prompt import MAIN_PROMPT, THINK_PROMPT
from ollama import chat
import threading
import time


def stream_thinking_prompt(model, stop_event):
    stream = chat(model=model, messages=[
        {
            'role': 'user',
            'content': THINK_PROMPT,
        },
    ], stream=True)
    print("🤔 Thinking...")

    for chunk in stream:
        if stop_event.is_set():
            break
        print(chunk['message']['content'], end='', flush=True)
        time.sleep(0.05)

    print("\n🤔 Thinking complete")


def stream_main_prompt(model, stop_event):
    stream = chat(model=model, messages=[
        {
            'role': 'user',
            'content': MAIN_PROMPT,
        },
    ], stream=True)
    for i, chunk in enumerate(stream):
        # stop thinking thread at first chunk
        if i == 0:
            print("main thread start")
            stop_event.set()
        print(chunk['message']['content'], end='', flush=True)
    print()


if __name__ == "__main__":
    MAIN_MODEL = "qwen2.5:7b"
    THINKING_MODEL = "qwen2.5:1.5b"

    stop_event = threading.Event()

    main_thread = threading.Thread(
        target=stream_main_prompt, args=(MAIN_MODEL, stop_event))
    thinking_thread = threading.Thread(
        target=stream_thinking_prompt, args=(THINKING_MODEL, stop_event))

    thinking_thread.start()
    time.sleep(1)
    main_thread.start()

    thinking_thread.join()
    main_thread.join()
