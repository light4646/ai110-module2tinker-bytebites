# Draft UML (first pass, no reference file)

This is the first diagram from a chat that only had `bytebites_spec.md` attached.
I'm keeping it to compare against the final design.

```mermaid
classDiagram
    class User {
        +int id
        +str name
        +str email
        +str password_hash
        +login()
        +logout()
    }
    class Customer {
        +list purchase_history
        +list favorites
        +is_verified() bool
    }
    class MenuItem {
        +int id
        +str name
        +float price
        +str category
        +float popularity
        +list allergens
    }
    class Menu {
        +list items
        +add_item(item)
        +filter_by_category(category) list
        +search(keyword) list
    }
    class Order {
        +int id
        +Customer customer
        +list items
        +str status
        +datetime created_at
        +compute_total() float
        +apply_discount(code)
    }
    class Payment {
        +float amount
        +str method
        +process()
    }
    class RecommendationEngine {
        +recommend(customer) list
    }

    User <|-- Customer
    Customer "1" --> "*" Order
    Order "*" --> "*" MenuItem
    Menu "1" o-- "*" MenuItem
    Order "1" --> "1" Payment
    RecommendationEngine ..> Menu
```

## Review notes

- **Adds classes that aren't in my candidate list:** `User`, `Payment`, `RecommendationEngine`.
- **Adds features the spec never asks for:** login and passwords, email, allergens, search, discounts, order status, timestamps, favorites.
- **Matches the spec:** `MenuItem` (name, price, category, popularity), `Menu` with `filter_by_category`, `Order` with `compute_total`, and `Customer` with `purchase_history`.
- **Verdict:** too big. The final design should keep only the four classes and the attributes the feature request describes.
