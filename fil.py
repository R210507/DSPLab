% Define frequency range
w = linspace(0, 10, 1000);

% Define denominator coefficients
a = [1 4 5];

% Define number of zeroes
num_zeroes = 3;

% Define zero locations
z = [-2, -4, -6];

% Initialize figure
figure;

% Loop through each zero
for i = 1:num_zeroes
    % Define numerator coefficients with current zero
    b = [1 z(i)];
    
    % Calculate frequency response
    H = (1i*w + z(i)) ./ ((1i*w + 2) .* (1i*w + 3) .* (1i*w + 5));
    
    % Plot frequency response
    subplot(2, 1, 1);
    plot(w, abs(H));
    hold on;
    xlabel("Frequency (rad/s)");
    ylabel("Magnitude");
    title("Frequency Response");
    
    subplot(2, 1, 2);
    plot(w, angle(H));
    hold on;
    xlabel("Frequency (rad/s)");
    ylabel("Phase (deg)");
    title("Phase Response");
end

% Legend for multiple zeroes
legend_zeros = cellstr(num2str(z'));
legend(legend_zeros);

% Display grid
grid on;
