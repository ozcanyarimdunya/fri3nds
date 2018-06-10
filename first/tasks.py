from time import sleep

from celery import shared_task, current_task


@shared_task
def simple_task(total):
    for num in range(total):
        sleep(0.2)
        percent = (float(num) / total) * 100
        current_task.update_state(
            state="PROGRESS",
            meta={"current": num, "total": total, "percent": round(percent, 2)}
        )

    return {"current": total, "total": total, "percent": 100}
