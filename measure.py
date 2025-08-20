from prompt import NEWS_PROMPT
from ollama import chat

import time

if __name__ == "__main__":
    model_lists = ["qwen2.5:0.5b", "qwen2.5:1.5b", "qwen2.5:3b", "qwen2.5:7b", "qwen2.5:14b"]

    for model in model_lists:
        print(f"{model}")
        start = time.time()
        stream = chat(model=model, messages=[
            {
                'role': 'user',
                'content': NEWS_PROMPT,
            },
        ], stream=True)

        chunk_times = []
        for chunk in stream:
            chunk_times.append(time.time() - start)

        if chunk_times:
            first_chunk_time = chunk_times[0]
            # Calculate intervals between chunks
            intervals = [t2 - t1 for t1, t2 in zip(chunk_times, chunk_times[1:])]
            avg_interval = sum(intervals) / len(intervals) if intervals else 0
            print(f"model: {model}, first chunk time: {first_chunk_time:.4f} seconds")
            print(f"average interval between chunks: {avg_interval:.4f} seconds")
            print(f"total chunks: {len(chunk_times)}")
        else:
            print(f"model: {model}, no chunks received.")
        
        end = time.time()
        total_time = end - start
        print(f"total time: {total_time:.4f} seconds")