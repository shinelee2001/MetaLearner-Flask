#include <iostream>
#include <fstream>
#include <filesystem>
#include <regex>
#include <unordered_map>
#include "md5.h"

namespace fs = std::filesystem;

// Hashes for known signatures.
// Later, will store them in a database
std::unordered_map<std::string, std::string>
    websell_signature = {
        {"hashforsomephp", "PHP webshell"},
        {"hashforsomeasp", "ASP webshell"},
        {"hashforsomejsp", "JSP webshell"}
};

bool detect_signature(const std::string& file_path){
    std::ifstream file(file_path, std::ios::binary);
    if (!file.is_open()) {
        return false;
    }

    std::string file_contents((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    MD5 hasher;
    std::string md5_hash = hasher.hash(file_contents);

    if (websell_signature.find(md5_hash) != websell_signature.end()) {
        return true;
    }
    return false;
}

bool detect_webshell(const std::string &file_path) {
    std::ifstream file(file_path);
    if (!file.is_open()) {
        return false;
    }

    std::string file_contents((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    if (std::regex_search(file_contents, std::regex("(system|eval|base64_decode)"))) {
        return true;
    }
    if (std::regex_search(file_contents, std::regex("(shell_exec|exec|passthru|proc_open|popen)"))) {
        return true;
    }
    return false;

}

void check_directory(const std::string &directory) {
    for (const auto &entry : fs::recursive_directory_iterator(directory)) {
        if (entry.is_regular_file() && (entry.path().extension() == ".php" || entry.path().extension() == ".php3" || entry.path().extension() == ".phtml")) {
            if (detect_webshell(entry.path().string()) || detect_signature(entry.path().string())) {
                std::cout << "Webshell detected in file: " << entry.path().string() << std::endl;
            }
        }
    }
    std::cout << "Finished checking directory: " << directory << std::endl;
}

int main() {
	std::string directory = "C:\\Users\\LG\\Desktop\\1_4_7_14\\uploads";
	check_directory(directory);
}