
# NeonFlux API Tester

**Author**: saladb0y  

NeonFlux is a Python-based API security testing tool designed for ethical hacking and vulnerability discovery. It includes tests for authentication enforcement, SQL injection, rate limiting, and endpoint discovery using a customizable wordlist. The tool is built to evade WAFs like Cloudflare with randomized delays and realistic HTTP headers.

---

## 📜 Features

- **Endpoint Discovery**: Uses a wordlist to find hidden API endpoints.
- **Authentication Enforcement Testing**: Checks for bypass vulnerabilities.
- **SQL Injection Detection**: Tests endpoints for common SQL injection flaws.
- **Rate Limiting Checks**: Simulates multiple requests to test rate-limiting mechanisms.
- **Verbose Mode**: Displays real-time logs of all tool actions for transparency.
- **WAF Evasion**:
  - Randomized delays between requests.
  - Realistic HTTP headers for anonymity.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/saladtosser/NeonFlux-API-Tester.git
   cd NeonFlux-API-Tester
   ```

2. **Install Required Dependencies**:
   Ensure Python 3.x is installed, then install the required libraries:
   ```bash
   pip install requests
   ```

---

## 🚀 Usage

1. **Run the Tool**:
   ```bash
   python neonflux.py
   ```

2. **Follow the Prompts**:
   - Enter the **base URL** of the API (e.g., `https://api.example.com`).
   - Provide the **wordlist path** for endpoint discovery or leave blank to manually input endpoints.

3. **Example**:
   - Base URL: `https://test.api-example.com`
   - Wordlist Path: `api_wordlist.txt`  

   Sample output:
   ```
   [!] Discovering Endpoints...
   [INFO] Checking: https://test.api-example.com/auth/login
   [FOUND] https://test.api-example.com/auth/login (200)

   [1] Testing Authentication Enforcement...
   [PASS] Authentication is enforced.

   [2] Testing SQL Injection...
   [FAIL] Potential SQL injection detected with payload: 1' OR '1'='1

   Testing complete. Results saved in 'neonflux_results.log'.
   ```

4. **Results**:
   - All results are saved to `neonflux_results.log`.

---

## 📂 File Structure

- **`neonflux.py`**: Main Python script.
- **`api_wordlist.txt`**: Wordlist for endpoint discovery.
- **`README.md`**: Documentation.

---

## ⚠️ Disclaimer

This tool is intended **only for educational purposes and ethical security testing**. It must be used **with proper authorization** from the target systems' owners.

- **Unauthorized use** of this tool is illegal and strictly prohibited.
- The author (saladb0y) is not responsible for any misuse or damage caused by this tool.

By using this tool, you agree to use it **responsibly** and only in environments where you have explicit permission to perform penetration testing.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🌐 Contact

- **Author**: saladb0y  
- **GitHub**: [https://github.com/saladtosser](https://github.com/saladtosser)
- **Instagram**: [https://Instagram.com/mydemiseismyown]

If you find any bugs, issues, or have suggestions for improvements, feel free to open an issue in the repository.

---

## 🏆 Contributions

Contributions are welcome! If you'd like to improve the tool:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Happy testing! 🚀
