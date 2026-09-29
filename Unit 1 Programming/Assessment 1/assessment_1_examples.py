# Runnable examples for Unit 1 Programming Implementation Assessment 1.


def learner_profile() -> tuple[str, int, bool]:
    # Each named variable stores a different data type from the assessment question.
    name = "Alice"
    age = 16
    is_student = True
    return name, age, is_student


def calculate_order_total(net_price: float, vat_rate: float = 0.20) -> float:
    # Sequence: these statements must run in order because each result is reused.
    vat_amount = net_price * vat_rate
    gross_price = net_price + vat_amount
    return round(gross_price, 2)


def lab_access_message(is_authorised: bool, is_isolated: bool) -> str:
    # Selection: the Boolean condition chooses the approved or blocked route.
    if is_authorised and is_isolated:
        return "Lab access approved"
    return "Lab access blocked"


def format_recent_alerts(alerts: list[str]) -> list[str]:
    # Iteration: the loop processes every KORA alert in the list once.
    formatted_alerts = []
    for alert in alerts:
        formatted_alerts.append(f"KORA alert: {alert}")
    return formatted_alerts


def main() -> None:
    # The main procedure calls each example and displays its result.
    name, age, is_student = learner_profile()
    print(f"Profile: {name}, age {age}, student={is_student}")
    print(f"Order total: GBP {calculate_order_total(50.00):.2f}")
    print(lab_access_message(is_authorised=True, is_isolated=True))
    for message in format_recent_alerts(["camera zone", "training complete"]):
        print(message)


if __name__ == "__main__":
    main()

